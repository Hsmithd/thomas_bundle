# Play: Banana - setup

- hosts: all
  become: false
  vars:
    app_name: "banana_app"
    retry_count: 3

  tasks:
    - name: Ensure cherry-task-1 is present
      ansible.builtin.file:
        path: /opt/banana/cherry-task-1
        state: directory

    - name: Template cherry-task-1 config
      ansible.builtin.template:
        src: templates/cherry-task-1.j2
        dest: /etc/banana/cherry-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure india-task-2 is present
      ansible.builtin.file:
        path: /opt/banana/india-task-2
        state: directory

    - name: Template india-task-2 config
      ansible.builtin.template:
        src: templates/india-task-2.j2
        dest: /etc/banana/india-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure india-task-3 is present
      ansible.builtin.file:
        path: /opt/banana/india-task-3
        state: directory

    - name: Template india-task-3 config
      ansible.builtin.template:
        src: templates/india-task-3.j2
        dest: /etc/banana/india-task-3.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure foxtrot-task-4 is present
      ansible.builtin.file:
        path: /opt/banana/foxtrot-task-4
        state: directory

    - name: Template foxtrot-task-4 config
      ansible.builtin.template:
        src: templates/foxtrot-task-4.j2
        dest: /etc/banana/foxtrot-task-4.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart banana service
      ansible.builtin.service:
        name: banana
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:43Z
