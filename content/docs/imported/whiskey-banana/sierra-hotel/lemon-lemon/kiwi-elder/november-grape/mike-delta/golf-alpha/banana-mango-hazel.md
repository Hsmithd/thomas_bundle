# Play: Banana - setup

- hosts: all
  become: true
  vars:
    app_name: "banana_app"
    retry_count: 4

  tasks:
    - name: Ensure date-task-1 is present
      ansible.builtin.file:
        path: /opt/banana/date-task-1
        state: directory

    - name: Template date-task-1 config
      ansible.builtin.template:
        src: templates/date-task-1.j2
        dest: /etc/banana/date-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure kilo-task-2 is present
      ansible.builtin.file:
        path: /opt/banana/kilo-task-2
        state: directory

    - name: Template kilo-task-2 config
      ansible.builtin.template:
        src: templates/kilo-task-2.j2
        dest: /etc/banana/kilo-task-2.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure mango-task-3 is present
      ansible.builtin.file:
        path: /opt/banana/mango-task-3
        state: directory

    - name: Template mango-task-3 config
      ansible.builtin.template:
        src: templates/mango-task-3.j2
        dest: /etc/banana/mango-task-3.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure uniform-task-4 is present
      ansible.builtin.file:
        path: /opt/banana/uniform-task-4
        state: directory

    - name: Template uniform-task-4 config
      ansible.builtin.template:
        src: templates/uniform-task-4.j2
        dest: /etc/banana/uniform-task-4.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart banana service
      ansible.builtin.service:
        name: banana
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
