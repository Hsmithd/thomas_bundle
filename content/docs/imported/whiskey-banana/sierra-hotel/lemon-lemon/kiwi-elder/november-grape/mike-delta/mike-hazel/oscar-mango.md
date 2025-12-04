# Play: Oscar - setup

- hosts: webservers
  become: false
  vars:
    app_name: "oscar_app"
    retry_count: 1

  tasks:
    - name: Ensure india-task-1 is present
      ansible.builtin.file:
        path: /opt/oscar/india-task-1
        state: directory

    - name: Template india-task-1 config
      ansible.builtin.template:
        src: templates/india-task-1.j2
        dest: /etc/oscar/india-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure delta-task-2 is present
      ansible.builtin.file:
        path: /opt/oscar/delta-task-2
        state: directory

    - name: Template delta-task-2 config
      ansible.builtin.template:
        src: templates/delta-task-2.j2
        dest: /etc/oscar/delta-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure kilo-task-3 is present
      ansible.builtin.file:
        path: /opt/oscar/kilo-task-3
        state: directory

    - name: Template kilo-task-3 config
      ansible.builtin.template:
        src: templates/kilo-task-3.j2
        dest: /etc/oscar/kilo-task-3.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart oscar service
      ansible.builtin.service:
        name: oscar
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:44Z
