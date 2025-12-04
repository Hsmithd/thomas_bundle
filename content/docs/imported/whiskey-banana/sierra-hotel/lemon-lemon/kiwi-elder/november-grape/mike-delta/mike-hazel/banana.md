# Play: Banana - setup

- hosts: all
  become: true
  vars:
    app_name: "banana_app"
    retry_count: 5

  tasks:
    - name: Ensure juliet-task-1 is present
      ansible.builtin.file:
        path: /opt/banana/juliet-task-1
        state: directory

    - name: Template juliet-task-1 config
      ansible.builtin.template:
        src: templates/juliet-task-1.j2
        dest: /etc/banana/juliet-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure delta-task-2 is present
      ansible.builtin.file:
        path: /opt/banana/delta-task-2
        state: directory

    - name: Template delta-task-2 config
      ansible.builtin.template:
        src: templates/delta-task-2.j2
        dest: /etc/banana/delta-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure juliet-task-3 is present
      ansible.builtin.file:
        path: /opt/banana/juliet-task-3
        state: directory

    - name: Template juliet-task-3 config
      ansible.builtin.template:
        src: templates/juliet-task-3.j2
        dest: /etc/banana/juliet-task-3.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart banana service
      ansible.builtin.service:
        name: banana
        state: restarted

## Notes

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:43Z
