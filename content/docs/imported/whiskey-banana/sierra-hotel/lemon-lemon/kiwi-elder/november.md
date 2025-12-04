# Play: November - setup

- hosts: webservers
  become: true
  vars:
    app_name: "november_app"
    retry_count: 4

  tasks:
    - name: Ensure india-task-1 is present
      ansible.builtin.file:
        path: /opt/november/india-task-1
        state: directory

    - name: Template india-task-1 config
      ansible.builtin.template:
        src: templates/india-task-1.j2
        dest: /etc/november/india-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure whiskey-task-2 is present
      ansible.builtin.file:
        path: /opt/november/whiskey-task-2
        state: directory

    - name: Template whiskey-task-2 config
      ansible.builtin.template:
        src: templates/whiskey-task-2.j2
        dest: /etc/november/whiskey-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure yankee-task-3 is present
      ansible.builtin.file:
        path: /opt/november/yankee-task-3
        state: directory

    - name: Template yankee-task-3 config
      ansible.builtin.template:
        src: templates/yankee-task-3.j2
        dest: /etc/november/yankee-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart november service
      ansible.builtin.service:
        name: november
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:43Z
